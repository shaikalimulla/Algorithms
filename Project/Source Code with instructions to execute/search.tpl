<!-- This file creates UI for Search page. Once user entered train number to search the entry in the system, 
this file creates a page to display train details to the user and provides a back button to redirect user to the home page -->

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
      .train {float:left; padding-top: 10px;}
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
      <div class="train">
        <h3>Train Details:</h3>
        %for name in train:
        <div class="name results">
        <table >
          <tr>
            <td><h5>Train Number: </h5> {{name[0]}}</td>
            <td><h5>Train Name:</h5> {{name[1]}}</td>
            <td><h5>Source Station: </h5> {{name[2]}}</td>
            <td><h5>Destination Station:</h5> {{name[3]}}</td>
            </tr>
      </table>
        </div>
        %end
      </div>
    </div>
  </body>
</html>