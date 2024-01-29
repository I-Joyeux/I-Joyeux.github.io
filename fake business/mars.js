

acres = parseFloat(
    prompt("How many acres do you want to purchase.", 1));
var average=parseFloat(acres*(6200*3.71))
    document.write(`<h2>cost for your land: $${average.toFixed(2)}</h2>`);
