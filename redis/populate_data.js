const csv = require('csvtojson')
const redis = require('redis')
const http = require('http')


// const redis_client = redis.createClient();

// var data = csv().fromFile('./../data/us-counties.csv').
// then((data)=>{
//     console.log(data)
// })

let res = http.get({
    host: 'http://localhost',
    port: '5984',
    path: '/covid/_all_docs'})

console.log(res)