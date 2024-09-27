// "Batch RGB Merge"

// Opens multiple sets of three separate color channels as
// an RGB stack or converts them to RGB images. File names
// ending in "d1", "d2" and "d0" are assumed to be red, green
// and blue channels respectively, but this can be changed in
// the dialog box.

// A sample image set, courtesy of Mikael Bjorklund, is available at:
//    http://rsb.info.nih.gov/ij/macros/images/DrosophilaCells.zip
// It consists of three images of Drosophila S2 cells,
// each with three channels (d0=blue, d1=red and d2=green  
// as indicated by the end of the filename. The staining is
// standard Hoechst, phalloidin, tubulin.

  Dialog.create("RGB Batch Convert");
  Dialog.addString("Red Suffix:", "_CH2");
  Dialog.addString("Blue Suffix:", "_CH1");
  Dialog.addCheckbox("Open as Stack", true);
  Dialog.show();
  redSuffix = Dialog.getString() + ".";
  blueSuffix = Dialog.getString() + ".";
  openAsStack = Dialog.getCheckbox();
  if (openAsStack)
      openImagesAsStack();
  else
      batchConvert();
  exit;

  function openImagesAsStack() {
      dir1 = getDirectory("Choose Source Directory ");
      dir2 = getDirectory("Choose Destination Directory ");
      list = getFileList(dir1);
      setBatchMode(true);
      n = list.length;
      if ((n%2)!=0)
         exit("The number of files must be a multiple of 2");
      stack = 0;
      first = 0;
      for (i=0; i<n/2; i++) {
          showProgress(i+1, n/2);
          red="?"; green="?"; blue="?";
          for (j=first; j<first+2; j++) {
              if (indexOf(list[j], redSuffix)!=-1)
                  red = list[j];
              if (indexOf(list[j], blueSuffix)!=-1)
                  blue = list[j];
          }
          open(dir1+red);
	  run("8-bit");
	  run("Red");
          open(dir1+blue);
	  run("8-bit");
	  run("Blue");
          run("Merge Channels...", "c1=["+red+"] c3=["+blue+"]  create");
	  Stack.setChannel(1);
	  setMinAndMax(0, 100);
	  Stack.setChannel(2);
	  setMinAndMax(0, 80);
	  Stack.setChannel(3);
	  setMinAndMax(0, 60);
	  Stack.setChannel(4);
	  setMinAndMax(0, 130);
          index = indexOf(red, redSuffix);
          name = substring(red, 0, index);
          saveAs("Tiff", dir2+name);
          first += 2;
      }
  }