# Atrybuty bezpieczeństwa informacji

- integralność - Zapewnia że informacja jest kompletna i nie została zmodyfikowana
    przez nieuprawnione osoby
- dostępność - Zapewnia, że dostęp do informacji nie zostanie utracony, a sama 
    informacja nie zostanie trwale zniszczona
- poufność - Zapewnia, że informacja nie zostanie udostępniona czy też upubliczniona 
    dla nieuprawnionych odbiorców

# Cele stosowania zabezpieczeń i zabezpieczenia (ISO 27001):

    5: Organizational controls

        5.1: Policies for information security
        5.2: Information security roles and responsibilities
        5.3: Segregation of duties
        5.4: Management responsibilities
        5.5: Contact with authorities
        5.6: Contact with special interest groups
        5.7: Threat intelligence
        5.8: Information security in project management
        5.9: Inventory of information and other associated assets
        5.10: Acceptable use of information and other associated assets
        5.11: Return of assets
        5.12: Classification of information
        5.13: Labelling of information
        5.14: Information transfer
        5.15: Access control
        5.16: Identity management
        5.17: Authentication information
        5.18: Access rights
        5.19: Information security in supplier relationships
        5.20: Addressing information security within supplier agreements
        5.21: Managing information security in the information and communication technology (ICT) supply chain
        5.22: Monitoring, review and change management of supplier services
        5.23: Information security for use of cloud services
        5.24: Information security incident management planning and preparation
        5.25: Assessment and decision on information security events
        5.26: Response to information security incidents
        5.27: Learning from information security incidents
        5.28: Collection of evidence
        5.29: Information security during disruption
        5.30: ICT readiness for business continuity
        5.31: Legal, statutory, regulatory and contractual requirements
        5.32: Intellectual property rights
        5.33: Protection of records
        5.34: Privacy and protection of personal identifiable information (PII)
        5.35: Independent review of information security
        5.36: Compliance with policies, rules and standards for information
        5.37: Documented operating procedures

    6: People controls

        6.1: Screening
        6.2: Terms and conditions of employment
        6.3: Information security awareness education and training
        6.4: Disciplinary process
        6.5: Responsibilities after termination
        6.6: Confidentiality or non-disclosure agreements
        6.7: Remote working
        6.8: Information security event reporting

    7: Physical controls

        7.1: Physical security perimeters
        7.2: Physical entry
        7.3: Securing offices, rooms and facilities
        7.4: Physical security monitoring
        7.5: Protecting against physical and environmental threats
        7.6: Working in secure areas
        7.7: Clear desk and clear screen
        7.8: Equipment siting and protection
        7.9: Security of assets off-premises
        7.10: Storage media
        7.11: Supporting utilities
        7.12: Cabling security
        7.13: Equipment maintenance
        7.14: Secure disposal or re-use of equipment

    8: Technological controls

        8.1: User end point devices
        8.2: Privileged access rights
        8.3: Information access restriction
        8.4: Access to source code
        8.5: Secure authentication
        8.6: Capacity management
        8.7: Protection against malware
        8.8: Management of technical vulnerabilities
        8:9: Configuration management
        8.10: Information deletion
        8.11: Data masking
        8.12: Data leakage prevention
        8.13: Information backup
        8.14: Redundancy of information processing facilities
        8:15: Logging
        8.16 Monitoring activities
        8.17: Clock synchronization
        8.18: Use of privileged utility programs
        8.19: Installation of software on operational systems
        8.20: Networks security
        8.21: Security of network services
        8.22: Segregation of networks
        8.23: Web filtering
        8.24: Use of cryptography
        8.25: Secure development life cycle
        8.26: Application security requirements
        8.27: Secure system architecture and engineering principles
        8.28: Secure coding
        8.29: Security testing in development and acceptance
        8.30: Outsourced development
        8.31: Separation of development, test and production environments
        8.32: Change management
        8.33: Test information
        8.20: Protection of information systems during audit testing

# Kryptografia i jej zastosowanie w ochronie przechowywanej i przesyłanej informacji:

## Algos

### Symmetric:

- DES
- AES

### Public key cryptography:

- RSA
- Eliptic Curve


# Uwierzytelnianie:

- hasło (sekrety)
- FIDO:
    - współdzielony sekret (Google authenticator)
    - Challenge-Response
    - cechy fizyczne

# IDS/IPS - Systemy wykrywania intruzów

An intrusion detection system (IDS) monitors traffic on your network, analyzes
that traffic for signatures matching known attacks, and when something
suspicious happens, you're alerted. In the meantime, the traffic keeps flowing. 

An intrusion prevention system (IPS) also monitors traffic. But when something
unusual happens, the traffic stops altogether until you investigate and decide
to open the floodgates again.

https://www.okta.com/identity-101/ids-vs-ips/


# Systemy kontroli dostępu do sieci (NAC):

https://www.cisco.com/c/en/us/products/security/what-is-network-access-control-nac.html

NAC pozwala kontrolować dostęp do całości lub części sieci określonym klientom.
Możemy przez to izolować telefony, IOT itp od infrastruktury krytycznej.

# Systemy zarządzania informacjami i zdarzeniami bezpieczeństwa (SIEM):

Combining security information management (SIM) and security event management
(SEM), security information and event management (SIEM) offers real-time
monitoring and analysis of events as well as tracking and logging of security
data for compliance or auditing purposes.

Put simply, SIEM is a security solution that helps organizations recognize
potential security threats and vulnerabilities before they have a chance to
disrupt business operations. It surfaces user behavior anomalies and uses
artificial intelligence to automate many of the manual processes associated
with threat detection and incident response and has become a staple in
modern-day security operation centers (SOCs) for security and compliance
management use cases.

https://www.ibm.com/topics/siem

# Zapory sieciowe nowej generacji (NGFW):

What is a next-generation firewall?

A traditional firewall provides stateful inspection of network traffic. It
allows or blocks traffic based on state, port, and protocol, and filters
traffic based on administrator-defined rules.

A next-generation firewall (NGFW) does this, and so much more. In addition to
access control, NGFWs can block modern threats such as advanced malware and
application-layer attacks. According to Gartner's definition, a next-generation
firewall must include:

 - Standard firewall capabilities like stateful inspection
 - Integrated intrusion prevention
 - Application awareness and control to see and block risky apps
 - Threat intelligence sources
 - Upgrade paths to include future information feeds
 - Techniques to address evolving security threats

 https://www.cisco.com/c/en/us/products/security/firewalls/what-is-a-next-generation-firewall.html#~choose-an-ngfw-firewall


# Bezpieczeństwo sieci bezprzewodowych:

## Attacking:


Wardriving is a technique used to identify and map vulnerable access points.
The name comes from the fact that attackers drive around a neighborhood and use
a laptop with a GPS device, antenna to identify and record the location of
wireless networks.  This technique is effective since many WiFi networks used
by businesses extend beyond the confines of the building and poor security
controls are applied to secure those networks.

Warshipping is a more efficient method of attacking WiFi networks as it allows
attacks to be conducted remotely, even if the attacker is not within range of a
WiFi network. The tactic was explained by IBM X-Force Red researchers at Black
Hat USA. They used cheap (under $100) and easy-to-obtain components to create a
single-board computer with WiFi and 3G capabilities that runs on a cell phone
battery. The device can be used to locally connect to the WiFi network and send
information back to the attackers via the 3G cellular connection.

Since the device is small, it can easily be hidden inside a small package, and
getting that package into a building is easy. It can just be mailed. Since the
package may be addressed to someone not working it the company, it could sit in
the mailroom for a while before it is opened. Since the package can be tracked,
the attackers will know when it is in the building. Alternatively, it could be
hidden in any number of items from plant pots to teddy bears. If the device is
within range of WiFi networks, it could be used to attack those networks.

Hashed network access codes can be sent back to the attackers to crack, and the
device can then connect to WiFi networks in the building and harvest data. The
device could be used in a man-in-the-middle attack by impersonating an internal
WiFi network.
MAC Spoofing

Many businesses use MAC filtering to prevent specific devices from connecting
to their WiFi networks. While this is useful for preventing individuals from
taking advantage of free WiFi for customers, this method of blocking users can
be easily bypassed. It is easy to spoof a MAC address and bypass this filtering
control.

- Kradzieże urządzeń

## Securing:

https://www.cisa.gov/uscert/ncas/tips/ST05-003

- Change default passwords. Most network devices, including wireless access
  points, are pre-configured with default administrator passwords to simplify
  setup. These default passwords are easily available to obtain online, and so
  provide only marginal protection. Changing default passwords makes it harder
  for attackers to access a device. Use and periodic changing of complex
  passwords is your first line of defense in protecting your device. (See
  Choosing and Protecting Passwords.)
- Restrict access. Only allow authorized users to access your network. Each
  piece of hardware connected to a network has a media access control (MAC)
  address. You can restrict access to your network by filtering these MAC
  addresses. Consult your user documentation for specific information about
  enabling these features. You can also utilize the “guest” account, which is a
  widely used feature on many wireless routers. This feature allows you to
  grant wireless access to guests on a separate wireless channel with a
  separate password, while maintaining the privacy of your primary credentials.
- Encrypt the data on your network. Encrypting your wireless data prevents
  anyone who might be able to access your network from viewing it. There are
  several encryption protocols available to provide this protection. Wi-Fi
  Protected Access (WPA), WPA2, and WPA3 encrypt information being transmitted
  between wireless routers and wireless devices. WPA3 is currently the
  strongest encryption. WPA and WPA2 are still available; however, it is
  advisable to use equipment that specifically supports WPA3, as using the
  other protocols could leave your network open to exploitation.  
- Protect your Service Set Identifier (SSID). To prevent outsiders from easily
  accessing your network, avoid publicizing your SSID. All Wi-Fi routers allow
  users to protect their device’s SSID, which makes it more difficult for
  attackers to find a network. At the very least, change your SSID to something
  unique. Leaving it as the manufacturer’s default could allow a potential
  attacker to identify the type of router and possibly exploit any known
  vulnerabilities.
- Install a firewall. Consider installing a firewall directly on your wireless
  devices (a host-based firewall), as well as on your home network (a router-
  or modem-based firewall). Attackers who can directly tap into your wireless
  network may be able to circumvent your network firewall—a host-based firewall
  will add a layer of protection to the data on your computer (see
  Understanding Firewalls for Home and Small Office Use).
- Maintain antivirus software. Install antivirus software and keep your virus
  definitions up to date. Many antivirus programs also have additional features
  that detect or protect against spyware and adware (see Protecting Against
  Malicious Code and What is Cybersecurity?).
- Use file sharing with caution. File sharing between devices should be
  disabled when not needed. You should always choose to only allow file sharing
  over home or work networks, never on public networks. You may want to
  consider creating a dedicated directory for file sharing and restrict access
  to all other directories. In addition, you should password protect anything
  you share. Never open an entire hard drive for file sharing (see Choosing and
  Protecting Passwords).
- Keep your access point software patched and up to date. The manufacturer of
  your wireless access point will periodically release updates to and patches
  for a device’s software and firmware. Be sure to check the manufacturer’s
      website regularly for any updates or patches for your device.
- Check your internet provider’s or router manufacturer’s wireless security
  options. Your internet service provider and router manufacturer may provide
  information or resources to assist in securing your wireless network. Check
  the customer support area of their websites for specific suggestions or
  instructions.
- Connect using a Virtual Private Network (VPN). Many companies and
  organizations have a VPN. VPNs allow employees to connect securely to their
  network when away from the office. VPNs encrypt connections at the sending
  and receiving ends and keep out traffic that is not properly encrypted. If a
  VPN is available to you, make sure you log onto it any time you need to use a
  public wireless access point.

# Przedstaw normy, standardy, dobre praktyki które wspomagają ocenę dojrzałości z zakresu cyberbezpieczeństwa aplikacji klasy internetowej klasy LMS (np. Moodle):

Istnieje wiele norm, standardów i dobrych praktyk, które mogą być stosowane do
oceny dojrzałości zabezpieczeń aplikacji internetowej typu LMS, takiej jak
Moodle. Niektóre z nich to:

OWASP Top 10: Ten dokument przedstawia 10 najważniejszych zagrożeń dla
aplikacji internetowych, w tym ataki na dane uwierzytelniające, ataki SQL
injection i ataki na sesję.

ISO 27001: Ten standard dotyczy zarządzania bezpieczeństwem informacji i może
być stosowany do oceny dojrzałości zabezpieczeń aplikacji internetowych.

NIST Cybersecurity Framework: Ten framework dostarcza praktycznych wytycznych
dla zarządzania bezpieczeństwem cybernetycznym, które mogą być stosowane do
oceny dojrzałości zabezpieczeń aplikacji internetowych.

SOC 2: Ten standard dotyczy kontroli bezpieczeństwa i prywatności danych i może
być stosowany do oceny dojrzałości zabezpieczeń aplikacji internetowych, które
przetwarzają dane wrażliwe.
