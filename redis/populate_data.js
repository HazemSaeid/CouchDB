const csv = require('csvtojson')
const redis = require('redis')


const redis_client = redis.createClient();

var data = csv().fromFile('./../data/us-counties.csv').
then((data)=>{
    console.log(data)
})
