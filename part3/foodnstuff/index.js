const express = require('express');
const app = express();
const path = require('path');
const axios = require('axios').default;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.json());
app.use(express.static(path.join(__dirname, 'pub')));

const getInventory = async () => {
    const res = await axios.get('http://localhost:8080/inventory')
    const inventory = await res.data.inventory.products
    return inventory;
}

const images = [ 'potato.jpeg', 'apple.jpeg', 'mango.jpeg' ];

const makePrice = ( num ) => {
return (Number.parseFloat(num).toFixed(2));
}

const capitalize = ( n ) => {
    return n[0].toUpperCase() + n.substring(1);
}

const makePretty = ( arr ) => {
    for(let i = 0; i < arr.length; i++){
    arr[i].image = images[i];
    arr[i].price = makePrice(arr[i].price);
    arr[i].name = capitalize(arr[i].name);
    }
   return arr;
}

const getQuote = async () => {
    const res = await axios.get('https://ron-swanson-quotes.herokuapp.com/v2/quotes')
    const quote = await res.data;
    return quote;
}

app.get('/whats-in-store', async (req, res) => {
    const inventory = await getInventory();
    makePretty(inventory);
    const quote = await getQuote();
    res.render('whats-in-store', { inventory, quote });
})

app.get('/', (req, res) => {
    res.render('home');
})

app.listen(3000, () => {
    console.log("Listening on port 3000...");
})

// app.get('/whats-in-store', async (req, res) => {
//     const res = await axios.get('http://localhost:8080/inventory')
//     console.log(inventory);
//     res.send('here is the inventory');
// })
