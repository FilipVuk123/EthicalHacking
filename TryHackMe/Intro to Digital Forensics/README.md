https://tryhackme.com/room/introdigitalforensics

# Introduction To Digital Forensics
Forensics is the application of science to investigate crimes and establish facts. With the use and spread of digital systems, such as computers and smartphones, a new branch of forensics was born to investigate related crimes: computer forensics, which later evolved into, digital forensics.


Think about the following scenario. The law enforcement agents arrive at a crime scene; however, part of this crime scene includes digital devices and media. Digital devices include desktop computers, laptops, digital cameras, music players, and smartphones, to name a few. Digital media includes CDs, DVDs, USB flash memory drives, and external storage. A few questions arise:

- How should the police collect digital evidence, such as smartphones and laptops? What are the procedures to follow if the computer and smartphone are running?
- How to transfer the digital evidence? Are there certain best practices to follow when moving computers, for instance?
- How to analyze the collected digital evidence? Personal device storage ranges between tens of gigabytes to several terabytes; how can this be analyzed?


More formally, digital forensics is the application of computer science to investigate digital evidence for a legal purpose.

### Q1. Consider the desk in the photo above. In addition to the smartphone, camera, and SD cards, what would be interesting for digital forensics?
laptop


# Digital Forensics Process
After getting the proper legal authorization, the basic plan goes as follows:

- Acquire the evidence: Collect the digital devices such as laptops, storage devices, and digital cameras. (Note that laptops and computers require special handling if they are turned on; however, this is outside the scope of this room.)
- Establish a chain of custody: Fill out the related form appropriately (Sample form). The purpose is to ensure that only the authorized investigators had access to the evidence and no one could have tampered with it.
- Place the evidence in a secure container: You want to ensure that the evidence does not get damaged. In the case of smartphones, you want to ensure that they cannot access the network, so they don’t get wiped remotely.
- Transport the evidence to your digital forensics lab.

At the lab, the process goes as follows:

- Retrieve the digital evidence from the secure container.
- Create a forensic copy of the evidence: The forensic copy requires advanced software to avoid modifying the original data.
- Return the digital evidence to the secure container: You will be working on the copy. If you damage the copy, you can always create a new one.
- Start processing the copy on your forensics workstation.

### Q1 It is essential to keep track of who is handling it at any point in time to ensure that evidence is admissible in the court of law. What is the name of the documentation that would help establish that?

Chain of Custody


# Practical Example of Digital Forensics
Everything we do on our digital devices, from smartphones to computers, leaves traces. Let’s see how we can use this in the subsequent investigation.


## Document Metadata
When you create a text file, TXT, some metadata gets saved by the Operating System, such as file creation date and last modification date. However, much information gets kept within the file’s metadata when you use a more advanced editor, such as MS Word. There are various ways to read the file metadata; you might open them within their official viewer/editor or use a suitable forensic tool. Note that exporting the file to other formats, such as PDF, would maintain most of the metadata of the original document, depending on the PDF writer used.


Let’s see what we can learn from the PDF file. We can try to read the metadata using the program pdfinfo

usage: pdfinfo DOCUMENT.pdf 

### Q1. Using pdfinfo, find out the author of the attached PDF file.
Ann Gree Shepherd


## Photo EXIF Data
EXIF stands for Exchangeable Image File Format; it is a standard for saving metadata to image files. Whenever you take a photo with your smartphone or with your digital camera, plenty of information gets embedded in the image. The following are examples of metadata that can be found in the original digital images:

Camera model / Smartphone model
Date and time of image capture
Photo settings such as focal length, aperture, shutter speed, and ISO settings
Because smartphones are equipped with a GPS sensor, finding GPS coordinates embedded in the image is highly probable. The GPS coordinates, i.e., latitude and longitude, would generally show the place where the photo was taken.

There are many online and offline tools to read the EXIF data from images. One command-line tool is exiftool. ExifTool is used to read and write metadata in various file types, such as JPEG images.

usage: exiftool IMAGE.jpg


### Q2. Using exiftool or any similar tool, try to find where the kidnappers took the image they attached to their document. What is the name of the street?

Milk Street

### Q3. What is the model name of the camera used to take this photo?

Canon EOS R6


# Tools used: exiftool, pdfinfo