# Web based GIS applications for field data gathering using mobile devices.


# Introduction
For the purposes of /cite the main paper/ a simple system of collecting and displaying geographical data had to be created. Its main goal was to utilize consumer grade equipment to facilitate the ease of conducting field measurements.

# Identification of challenges and requirements.
The main goals of the application is to store files containg measurements with the assorted metadata in a central location, while also providing an ability to view the gathered data on a map. 

Such an application should also be easy to use, easy to maintain and easy to update if problems are encountered while a measuring team is in the field.

## Chosen architecture

The solution is a web application that uses a traditional centralized backend to store the data. Such architecture allowed to easily deploy changes to end users while they are in the field, and the development team was familiar with it the most. One drawback of such a solution is the need for a constant internet connection for the measuring team. As the research would be conducted in an urban environment, such a compromise was acceptable.

The data visualization layer has a different usecase, as it is publicly available. As such it was developed as a separate project, using the same backend to share the data, without any ability to modify the data.

## Location on consumer grade mobile phones
One limitation encountered in the project, was the staleness of location data provided by consumer mobile devices. Due to the limitations of our chosen architecture we were unable to access the GPS hardware directly. Therefore, we developed two solution to this problem.

### Web Geolocation API
/cytowanie dokumentacji mozilla https://developer.mozilla.org/pl/docs/Web/API/Geolocation_API /
The browser exposes geolocation data to the web applications by the Geolocation API. It allows the application to request location information if the user allows it. As this is a high level abstraction, the application does not have any control over the way the location is acquired. It can be valid GPS data, or it can be derived from an IP address if the device lacks any other way to query location information.

Another limitation is lack of control over any caching of the location data. Browser vendors, in an effort to reduce energy consumption may only query GPS data every couple of minutes. Due to this cache, our web application queries the browser several times to get the latest information.

Some institutions might find it difficult to comply with the requirement for secure `https` context while using Geolocation API, as it requires proper setup of the hosting infrastructure with SSL certificates.

### EXIF

One workaround involved searching for embedded location data in images, as specified by the EXIF specification /cite EXIF spec/. We were able to conduct successful tests, that showed that consumer Xiaomi smartphones ware able to provide location accurate to hundredths of arc seconds.

However, like in the previous strategy, the process of encoding location is implemented by the device's vendor, we also discovered that location data could be cached by the device, thus resulting in old location being encoded in new measurements. Some devices also lack the ability to encode any location information.

Another limiting factor in this method ware the privacy protecting mechanisms present in some software, that stripped location data from photos taken directly in web browsers.


# Tooling

The choice of tooling is mostly based on the familiarity of the development team. We chose python for the language of our backend services, as our familiarity with it allowed us to implement the solution in requested time frame.

## Frontend

We had decided to write both user-facing parts of our web application using the `react` framework. The decision to use it over competing `angular`, as more of our development team members were proficient with it.

However, another framework that we failed to include in our decision-making process was `solid.js`. It's ability to store state globally without any special requirements could have been useful, however none of us have ever worked with it as it is quite new. Future small data gathering application could make use of it.

## Backend

One challenge in developing the backend services for our web application was the lack of budget for a dedicated server or cloud infrastructure. However, we were able to use a retired enterprise server with a residential internet connection, due to it being owned by one of the developers.

The processing power was not the limiting factor compared to the residential fiber optic internet connection. This limitation forced us to implement transcoding process for audio recordings and image files.

For the backend framework we chose `FastApi`, as our development team wanted to gain real project experience in it. A fullstack framework like `django` could have been a better choice, but we decided against choosing it due to personal reasons.

### Background tasks
/link to https://geek.justjoin.it/dramatiq-jako-kolejka-zadan-jak-usprawnic-skalowanie-systemu /

To handle file operations and external API integration we used `dramatiq`. It allowed us to run expensive transcoding operations in another service, freeing up the main application to serve requests without interruption. 

In retrospective, it might have been sufficient to use built in background tasks in `FastAPI`, as our low volume of requests and comparatively high processing power allows us to transcode all media files in seconds.

#### File compression

One of the most important background tasks involved lowering the size of files, and as a result the used bandwidth on our limited internet connection, without sacrificing the quality of the data too much.

For images, we used `imagemagick` to lower the resolution by a factor of 5. Together with the use of a more efficient `webp` codec, we were able to drop the file size on average by 95%, as a result precompresing the images only increased the storage requirements of our backend services by 5% per image. 

One of unforeseen challenges involved in transcoding the images was the need of special handling for rotation information. Some mobile devices always encode the images in the same orientation, but store additional information about presentation orientation in EXIF metadata. As a result we had to parse this information and rotate the images accordingly.

Audio file transcoding was implemented using the `ffmpeg` utility. The source files ware uncompressed `wave` files, which we choose to transcode to the `aac` codec in `adts` format.(footnote: `adts` format uses the `.aac` file extension) We used the bitrate of 128 kilobits per second as a good compromise between file sizes and quality. We also used transparent filesystem compression to reduce the size of original files offered by `ZFS`. Due to the above strategies we were able to also drop the file sizes by 95%, just like in the case of images.

The combination of those strategies meant that all the files generated and recorded consumed around 3 gigabytes of storage space.

### Database schema
We used the `postgresql` database and `sqlAlchemy` object relational mapper to store our data. We also used `redis` to cache requests and for scheduling background tasks for `dramatiq`.

Furthermore, we did not use `postgresql` to store files, which were stored with temporary filenames in form of their unique IDs. The original filenames were restored when they were sent to the web applications. This allowed us to store files with non-unique names along with assorted `mime` information which had allowed us to sort them by types.

## Details on our deployment

The application is hosted on a dell r720 server located in the basement of one of the authors. As a result `ssl/tls` configuration necessary for proper functioning is not included in this application, as it was handled externally using a properly configured `nginx` server to proxy all the requests to the backend services.

Additionally, to ease the burden of hosting large files, the application is proxied through `cloudflare` services. Although this would be unnecessary when using a university network, we were unable to use one. This has resulted in some limitations for the measurement procedure, as `cloudflare` only allows attachments of up to 100mb on the cheapest tier of service. Due to this limitation, the measuerement team was required to keep their measurements to be around a minute in length.


# Operation of the services
## Microservice architecture

We divided our application into several services:
- nginx service - Acted as a reverse proxy to the backend service and hosted static files for our web applications. Prevented non-internal access to the registration page and API documentation.
- backend service - The main `FastAPI` application serving requests and authenticating users.
- worker service - The `dramatiq` task runner that had access to `ffmpeg` and `imagemagick` for file transcoding, was also responsible for querying weather information from `openwheathermap`.
- db service - The `postgresql` database.
- redis service - The `redis` database for caching and event queue for `dramatiq`.
- pgadmin service - Instance of `pgadmin` for database administration and maintenance.

## Continuous integration and deployment.

We made heavy use of `github actions` in our development process. This has allowed us to automatically build our services to containers on every code change. Those built services would get tagged with the number of the connected pull request and would be uploaded to `docker hub`.

This has allowed us to download the latest changes onto our production server by changing the branch of the relevant service and running two commands. Unfortunatly we have failed to introduce automatic deployments, so this simple process had to be done manually. 

Such a workflow might seem like overkill for a small application like ours, however it has the benefit of allowing easy rollbacks and fixes if during field measurements a problem is found.

# Redistribution

The source code for the complete application is available on [GitHub](https://github.com/HakierGrzonzo/PBL-polsl-2022) under the GNU General Public License Version 2, a copy of the license is attached to the code.

The code itself is written and documented in English, however commit messages are in Polish, as they were parsed for the purpose of auto-generating time tracking cards for university administration.


## Project structure
The project is divided into several folders:
- `./backend/` - All the backend related services reside there.
- `./frontend/map` - The root of the public view.
- `./frontend/editor` - The root of the private view.
- `./dev_proxy` - Useful reverse-proxy used for the development. Merges development environments for frontend applications with the backend to avoid problems related to third party cookie restrictions.
- `./ionic` - A prototype mobile application for data gathering.
- `./worksheet_generator` - python scripts to generate paperwork for the university administration in LaTeX.

### Required third party API tokens

In the file `api-keys.env` the following private `api keys` have to be supplied:
- `OPEN_WEATHER_MAP` - [OpenWheatherMap](https://openweathermap.org/)




