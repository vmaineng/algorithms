//URL Shortener

function shortenURL(url) {
  const urlDatabase = new Map();

  function encode(longUrl) {
    let shortUrl = generateRandom(6);
    while (urlDatabase.has(shortUrl)) {
      shortUrl = generateRandom(6);
    }
    urlDatabase.set(shortUrl, longUrl);
    return shortUrl;
  }

  function decode(shortUrl) {
    return urlDatabase.get(shortUrl) || null;
  }

  function generateRandom(length) {
    const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let result = "";
    for (let i = 0; i < length; i++) {
      result += char[Math.floor(Math.random() * chars.length)];
    }
    return result;
  }
}

console.log(shortenURL("https:google.com"));
