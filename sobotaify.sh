#!/usr/bin/bash
make clean
cat > projekt.cbp <<EOF
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<CodeBlocks_project_file>
	<FileVersion major="1" minor="6" />
	<Project>
		<Option title="GrzegorzKoperwas" />
		<Option pch_mode="2" />
		<Option compiler="gcc" />
		<Build>
			<Target title="Debug">
				<Option output="bin/Debug/test" prefix_auto="1" extension_auto="1" />
				<Option object_output="obj/Debug/" />
				<Option type="1" />
				<Option compiler="gcc" />
				<Compiler>
					<Add option="-g" />
				</Compiler>
			</Target>
			<Target title="Release">
				<Option output="bin/Release/test" prefix_auto="1" extension_auto="1" />
				<Option object_output="obj/Release/" />
				<Option type="1" />
				<Option compiler="gcc" />
				<Compiler>
					<Add option="-O2" />
				</Compiler>
				<Linker>
					<Add option="-s" />
				</Linker>
			</Target>
		</Build>
		<Compiler>
			<Add option="-Wall" />
		</Compiler>
EOF
tree -inf | grep -E '*.cpp|*.hpp' | while read file; do
	echo '<Unit filename="'$file'" />' >> projekt.cbp
done
cat >> projekt.cbp <<EOF
		<Extensions />
	</Project>
</CodeBlocks_project_file>
EOF
echo "Project was built, zipping it"
rm GrzegorzKoperwas.zip
zip GrzegorzKoperwas.zip *