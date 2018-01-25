<h1>Triangle Center Program in Python</h1>
<strong>by: Lachi Balabanski</strong>

<h2>Information:</h2>
<p>Two important centers of triangles are the circumcenter and centroid. The circumcenter is found by constructng perpindicular bisectors from two or more sides of the triangle and finding their intersection. The circumcenter of a triangle is found by creating medians form two or more sides of the triangle and finding their intersections. Medians are lines that pass through the midpoint of two of the triangle's points and opposite vertex of a triangle</p>

<p>The circumcenter is important, because it is equidistant from all points on the triangle. For instance, a park owner would want to place the bathrooms equidistant from his three rides. He would need to locate the circumcenter for the exact location of his bathroom.</p>

<p>The centroid is important, because it is the center of mass or center of gravity for a triangle of uniform density.</p>

<p>This repo was created as an exercise in matplotlib and numpy</p>

<h2>Use:</h2>
<p>The parameters are:</p>

<ul>
	<li>Point1(-p1): The first point of the triangle. Give as a comma seperated string of numbers <i>i.e. "2,3"</i> </li>
	<li>Point2(-p2): The second point of the triange. Same as point one</li>
	<li>Point3(-p3): The third point of the triangle. Same as points two and one</li>
	<li>Show(-s): Displays the graph. Give as a python boolean <i>i.e. "True"</i> *Only not required field*</li>
	<li>Type(-t): The type of center you want to calculate. Give as string either <i>"circ"</i> or <i>"cent"</i> where circ is the circumcenter and cent is the centroid</li>
</ul>

<p><strong>IMPORTANT:</strong> When giving negative numbers replace the negative sign '-' with '~'</p>

<p>An example for generating a graph of the triangle and circumcenter for the triangle with points (2,3), (-1,0), (4,1):</p>

<code>$python main.py -p1 2,3 -p2 ~1,0 -p3 4,1 -s True -t circ</code>

<p>Thank you for using my triangle repository!</p>
