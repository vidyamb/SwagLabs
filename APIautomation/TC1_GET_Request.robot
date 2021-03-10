
library   RequestLibrary


${base_url}  https://www.googleapis.com/youtube/v3
${value}  channels?part=contentDetails&mine=true


get_YouTubeInfo
   create  session mysession  ${base_url}
   ${reponse} =  get request mysession  ${value}
   log to console   ${response.status_code}
   log to console   ${response.content}
   #log to console   ${response.headers}