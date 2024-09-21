// Define directories for images and ROIs
dir = getDirectory("Choose the directory containing images and rois");

// Specify file extensions for images and ROIs
imageExt = ".tif";  // Adjust as needed
roiExt = "_rois.zip";   // Adjust as needed

// Set desired measurements
run("Set Measurements...", "area mean standard min integrated display redirect=None decimal=3");

// Process all files in the directory
list = getFileList(dir);

// Process each image and corresponding ROI file
for (i = 0; i < list.length; i++) {
	  filename = list[i];
	  if (endsWith(filename, imageExt)) {
	  	// Open the image
	  	open(dir + filename);
	  	// Open the corresponding ROI file
	  	roiFilename = replace(filename, imageExt, roiExt);
	  	open(dir + roiFilename);
	  	// Measure intensities on each channel
	  	for (c = 1; c <= 2; c++) {
	  		selectWindow(filename);
	  		setSlice(c);
	  		roiManager("Measure");
	  		}
	  	// Close image and reset ROI manager
	  	close();
	  	roiManager("reset");
	  	}
}
