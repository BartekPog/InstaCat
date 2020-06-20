
curl --output cat.jpeg 'https://thiscatdoesnotexist.com/' \
  -H 'authority: thiscatdoesnotexist.com' \
  -H 'cache-control: max-age=0' \
  -H 'dnt: 1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'accept-language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'cookie: __cfduid=d5ce345f663f9d25ae8a5ce91396750121592664875' \
  --compressed



curl --output text-response.txt \
    -F 'text=@prompt.txt' \
    -H 'api-key:quickstart-QUdJIGlzIGNvbWluZy4uLi4K' \
    https://api.deepai.org/api/text-generator 