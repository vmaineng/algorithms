function domainName(url){
    //iterate through entire array until after //
    //push into a new string
    //until you reach com

// url = url.replace("http://", "") 
// url = url.replace("https://", "") 
// url = url.replace("www.", "") 
// return url.split(".")[0]

url = url.toString().replace('https://', '').replace('http://', '').replace('www.', '');

return url.split('.')[0];

  }

  console.log(domainName("http://github.com/carbonfive/raygun"))