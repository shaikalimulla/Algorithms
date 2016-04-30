<!-- This file creates UI for Home Page. Uses html forms to create the home page -->

<html>
  <head>
    <title>Welcome to Indian Railway Inquiry!</title>
    <style type="text/css">
      body {font-family:sans-serif;color:#4f494f;}
      cent {text-align: center}
      form input {border-radius: 7.5px;color:#000000;}
      h5 {display: inline;}
      h3 {color:brown}
      .label {text-align: right}
      .name {width:100%;float:left; padding:3px;}
      .wrapper { padding-left: 25px; padding-top: 10px}
    </style>
  </head>

  <body>
    <div class="wrapper">
      <h1>Welcome to Indian Railway Inquiry!</h1>
      <div align=center>

      <form method="post" class="form" action="/insert" method='post' autocomplete="off" style="background-color:grey">
		<h3>Insert Train Details Here!!!</h3> 
		
		<table>
		    <tr>
		      <td align="right" style="background-color:lightgreen">Enter Train Number: </td>
		      <td align="left"><input type="text" value="" name="trainNo" required/></td>
		    </tr>
		    <tr>
		      <td align="right" style="background-color:lightgreen">Enter Train Name: </td>
		      <td align="left"><input type="text" value="" name="trainName" required/></td>
		    </tr>
		    <tr>
		      <td align="right" style="background-color:lightgreen">Enter Source Station: </td>
		      <td align="left"><input type="text" value="" name="srcStn" required/></td>
		    </tr>
		    <tr>
		      <td align="right" style="background-color:lightgreen">Enter Destination Station: </td>
		      <td align="left"><input type="text" value="" name="dstStn" required/></td>
		    </tr>

		  </table>		
		      <input type="submit" value="Insert Train Details" style="background-color:maroon"/>
      </form>
		<br><br>

      <form method="post" class="form" action="/trainNo" method='post' autocomplete="off" style="background-color:grey">
		<h3>Search for Train Details Here!!!</h3> 

		<table >
		    <tr>
		      <td align="right" style="background-color:lightgreen">Enter Train Number: </td>
		      <td align="left"><input type="text" value="" name="trainNo" required/></td>
		    </tr>
		  </table>		
		      <input type="submit" value="Search for Train Details" style="background-color:maroon"/>
	      
      </form>
		<br><br>

      <form method="post" class="form" action="/deleteTrainNo" method='post' autocomplete="off" style="background-color:grey">
		<h3>Delete Train Details Here!!!</h3> 
		
		<table>
		    <tr>
		      <td align="right" style="background-color:lightgreen">Enter Train Number: </td>
		      <td align="left"><input type="text" value="" name="trainNo" required/></td>
		    </tr>
		    </table>	
		      <input type="submit" value="Delete Train Details" style="background-color:maroon"/>
      
      </form>
		<br><br>
		
      <form method="post" class="form" action="/show" method='post' style="background-color:grey" align = "center">
       <h3>View All Train Details Here!!!</h3> 
      
        <input type="submit" value="Show All Train Records" name="show" style="background-color:maroon"  />
      </form>
		<br><br>
		      
      </div>
        %end
      </div>
    </div>
  </body>
</html>