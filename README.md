# TopographicAnalysisTool
Topographic analysis tool that produced customised raster datasets essential for topographic analysis

GETTING STARTED

The general file layout used for this example

•	Aspect: Folder that holds the aspect raster data
•	Contours: File to hold contour data that needs to be supplied by the user
•	Raster: File to hold elevation raster data
•	Style: File that holds data on the colours scheme for reclassed rasters
•	Tools: File that holds the reclassification tool

Files that have been supplied

•	MajorProject.py - the code for the project
•	reclassTool.py – the code for creating class rules
•	The colour ramp files in the styles folder – can be changed if a different colouring style is required
•	Class rules in the rules folder – Supplied to show an example of the layout required. These need to be changed based on the required classes.

Files that need to be supplied

•	A contours shapes file

How to organise files

•	All EL_COUNTOUR files should be placed in the Contours folder
•	All ColourRamp.qml files need to be placed in the Styles folder
•	All rules.txt files need to be placed in the rules folder
•	ReclassTool.py can be placed in the tools folder for better organisation
•	All other outputs should be directed to their respective folder

GUIDELINES FOR USING RECLASSIFICATION TOOL

Step 1 – 

•	Run section 1 of code to obtain the mix and max values of the elevation raster
•	Refer to “guidelines for using the code” 

Step 2 – 

•	Open the reclassTool python file with a program that allows you to run the file in a kernel.
•	Run the code and enter the parameters asked (min, max and number of classes wanted)
•	Number of classes will be the number of class breaks outputted

Step 3 –

•	After running and entering the values the console will return the required format for the class breaks. This is the text below **the following are the class breaks** text.
•	The final row should be * = NULL
•	Copy all the text and paste it into the ElevRules txt file
•	Now that the reclass rules have been defined, continue with section 2 of the code

GUIDELINES FOR USING CODE

Step 1 – Define file paths and other parameters

•	Using the code as a guideline, define the required file paths for the project
•	Each required file path has already been defined, only the path needs to be updated
•	Each file path contains an explanation for what its purpose is if it becomes confusing
•	Define the raster pixel size (resolution) of the elevation raster that will be processed
•	Input True or False for each output that you want (reclassed elevation, aspect raster, shaded relief and so on). Putting False will skip the processing.

Step 2 – Copy and paste section 1 of code

•	The first section should be copy and pasted only if you want the elevation raster to be reclassified. Otherwise, you can continue by entering in the entire code into the python console
•	When entering section 1 it will ask for the coordinate reference system which needs to be selected
•	Once section 1 has been completed, it will return the min and max values of the elevation raster
•	Use these min and max values for the reclassification tool
•	Copy and paste the classes into the elevation classes txt file that was defined

Step 3 – Proceed with section 2 of code

•	The final section can all be copy and pasted into the console for the final processing
•	The result will be the elevation raster by default and the other outputs depending on which ones you chose


