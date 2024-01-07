const axios = require('axios');


let token = '9baf6a72840f14b2653b0f8904788a6736b096b6'
axios.put('http://127.0.0.1:8000/api/posts/3/',{
    title: 'hi',
    body: 'hello worlds',
    publish: 'p',
    views: 1
}, {
    headers: {
        "Authorization": 'Token ' + token
    }
}
    , function (resp) {
        console.log(resp.data)
    }).then((err) => {
        console.log(err)
    })

