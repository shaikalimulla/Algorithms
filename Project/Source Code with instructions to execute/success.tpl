<!-- This file creates UI to display success message to the user. Once user entered train number to insert the entry and 
system did update entry, this file creates a page to display a success message to the user that entered train number 
is inserted successfully into the system and provides a back button to redirect user to the home page -->

<html>
  <head>
    <title>Welcome to Indian Railway Inquiry!</title>
    <style type="text/css">
      body {font-family:sans-serif;color:#4f494f;}
      form input {border-radius: 7.5px;}
      h5 {display: inline;}
      table,th {border: 1px; }
      td {padding: 15px;}
      .label {text-align: right}
      .gap {float:left; padding-top: 40px;}
      .name:nth-child(odd){background-color:#bfbfbf;} 
      .name:nth-child(even){background-color:#f2f2f2;}
      .results {width:100%;float:left; padding:3px;}
      .wrapper { padding-left: 25px; padding-top: 20px}
    </style>
  </head>

  <body>
    <div class="wrapper">
      <h1>Welcome to Indian Railway Inquiry!</h1>
        <form class="form">
        <input type="button" value="Go back to Home Page" onClick="history.go(-1);return true;"/>
      </form>
		<div class="gap">
			Result:
		      <div class="name results">
		      		<p> Successfully Inserted train details!!! </p>
		      </div>
		  </div>    		
    </div>
  </body>
</html>