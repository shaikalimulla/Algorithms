<!-- This file creates UI to display all the train records in the system. If user wants to know all the records then it can be 
viewd using "display all train details" option in the home page and when user enters that option, this file creates a page to 
display all the records present in the system to the user and provides a back button to redirect user to the home page -->

<html>
  <head>
    <title>Welcome to Indian Railway Inquiry!</title>
    <style type="text/css">
      body {font-family:sans-serif;color:#4f494f;}
      form input {border-radius: 7.5px;}
    </style>
  </head>
	
  <body>
    <div class="wrapper">
      <h1>Welcome to Indian Railway Inquiry!</h1>
        <form class="form">
        <input type="button" value="Go back to Home Page" onClick="history.go(-1);return true;"/>
      </form>
    </div>
  </body>

<pre>
{{content}}
</pre>
  
</html>