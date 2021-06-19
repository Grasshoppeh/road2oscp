Installing on VM

# Installing Kali Linux on a Virtual Machine

1. Download and install Virtualbox and the latest Kali linux image
2. Load up virtual box and create a new machine
	-  Set the Operating system to debian 64-bit
	-  Set Memory to 8gb (I've have a lot of resources)
	-  Create a virtual disk for 80gb and leave the dynamic sizing on
	-  Create it
3. Change the default settings for kali
	- General > Advanced, turn on bi-directional pasting and drag and drop
	- System > Motherboard, Set disk and optical to top
	- System > Proccessor, Give the system 4-6 cores (YAY AMD)
	- Display > Screen, Set video memory to 128mb
	- finish
4. Launch the virtual machine and set the kali iso as the target
5. Do boring setup IT stuff.........
7. After you login `sudo apt update && apt upgrade`
8. Run the fixes here for virtual machines [pimpmykali](https://github.com/Dewalt-arch/pimpmykali)
	-	Note: personal preferance I like segmented users, I pressed no on making root default 