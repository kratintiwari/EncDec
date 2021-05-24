# EncDec
<b><u>Tool based in python to url encode and decode string.</b></u>
<hr>
<h2>INSTALLATION AND USAGE</h2>

Requires python 3.7 or higher

Install with git: git clone <b>https://github.com/kratintiwari/EncDec.git<b>

Go to folder 
  
  Run with python3 command : python3 encdec.py -options
  
  <h4>OPTIONS</h4>
    <ul type='ul' style='disc'>
  <li>-h  :  help option (encdec.py -e 'string to URLencode' / encdec.py -d 'string to URLdecode' )</li>
  <li>-e  :  encode option ( -e 'string to urlencode' )</li>
  <li>-d  :  decode option ( -d 'encode string to decode into plain text' )</li>
      </ul> 
      <hr>  
  
<h2>EXAMPLES</h2>
  
  python3 encdec.py -e 'https//xyz.com/?go_to=javascript:alert('1')'

  <h4>RESULT</h4>
  -------------------<br>
  https%2F%2Fxyz.com%2F%3Fgo_to%3Djavascript%3Aalert%281%29<br>
  -------------------
  <br>
  <br>
  python3 encdec.py -d 'https%2F%2Fxyz.com%2F%3Fgo_to%3Djavascript%3Aalert%281%29'
    
  <h4>RESULT</h4>
  -------------------<br>
  https//xyz.com/?go_to=javascript:alert('1')<br>
  -------------------
  
<hr>  
<h2>LICENSE</h2>

Copyright (c)  Kratin Tiwari <a href="mailto:kratintiwari8@gmail.com">kratintiwari8@gmail.com</a> 
<br>
Licencse : GNU General Public License  

<hr>  
