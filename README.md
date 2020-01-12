# DICON to PNG conversion

[Someone flew over a median and hit me](https://www.youtube.com/watch?v=302QaUchRq8) December 20th 2019. After we'd towed the car and talked to the police and made all the requisite calls, my mother insisted I go to the ER to be checked out for slight neck/upper back pain. They took some xrays showing nothing broken. The Model 3 really is a safe car. I asked whether I could have the images, since it's a rare opportunity to see inside myself, and the tech told me yes, but I'd have to call later, and due to HIPAA I'd have to come in person, show ID, and sign a release.

When I showed up at the hospital a few days later, they handed me a CD. The only computer capable of reading a CD at the house was a really old Mac, and I was dismayed to find the CD full of clutter meant to support a specialized `.exe` Sectra viewer program and nothing resembling my xrays in a familiar image or document format. I could at least put the files on a USB drive, but I didn't have a Windows machine of my own to run the `.exe`, so I waited a while before considering the jumble again.

Eventually I stumbled across mention of `DICOM` files as a medical imaging standard, and there was a folder just called `DICOM` with what could be image files inside several additional layers of folders. I tried uploading these files to file conversion websites, but not all of them worked, and they were slow, and one of the images was just too big to handle. Some searching led me to discover that someone has written a Python library for handling these, and conversion is very simple. Then [the code](convert.py) took all of a few minutes. I release it for the world here because this took me longer to figure out than it should have.

![mouth](EE0BCB6F.png)
This was a last extra. He had me open my mouth so he could see the front of some of my upper vertebrae through the aperture between my teeth.

It's also extra freaky, like something out of Alien.

![elongated neck](EE542215.png)
Angelic glowing thing on the end of swan neck.

![twisted](EEBE3953.png)
The suture across my right skull really stands out.

I wonder where the bones in my midface are. Is the sinus cavity really that big? Is my maxilla just really out of focus?

![slouched profile](EEFA9DCA.png)
The xray tech told me to slouch for this one: "the complete opposite of what your mother always told you"

You can see my hyoid really clearly, as well as the filling in my right, lower, rearmost molar, and the bony bridge of my nose, and a bit of my hair. Good to see my mandible isn't flattened out much.
