# Droplet Size Distribution Determination

## Comments
Script used during the work as a researcher in Federal University of Espirito Santo (Universidade Federal do Espírito Santo) to create a histogram for the droplets size distiribution of emulsions

## Input data
_A .TXT file with the diameters of the droplets arranged in a array form._

## Output data
The output data consists  in two files: 

_i) A .PNG file -- Graph containing: Histogram of droplet size distribution, a line plot with cumulative frequency and a representation of <html>d<sub>90</sub></html>._

_ii) A .XLSX file -- Data file containing: original input data (droplets diameters), the bins used in the histogram, the relative and cumulative frequencies, and the <html>d<sub>90</sub></html> value as well._ 

# Input data and Output data examples

In this section we can see bellow the input data used, and the output data obtained using the script **"script_dsd_plot.py"**. Click on the images if you wish to see them at the original size. Fig. (1) shows the input data as a .TXT file and Figs. (2) and (3) shows the output data.

# Input data example
<img src="https://i.ibb.co/3sWTQ2b/input-example.png" width="45%" height="45%" alt="Input data example">
<p>Figure 1. Input data example.</p>


# Output data example
<img src="https://i.ibb.co/xmJPqgK/output2-example.png" width="50%" height="50%" alt="Output data example">
<p>Figure 2. Output data example: Graph.</p>
     
<img src="https://i.ibb.co/jWr3ZYy/output1-example.png" width="50%" height="50%" alt="Output data example">
<p>Figure 3. Output data example: Data file: .XLSX.</p>

# Solution

To achieve the results shown above I used the modules: Numpy, Matplotlib and Xlsxwriter.
