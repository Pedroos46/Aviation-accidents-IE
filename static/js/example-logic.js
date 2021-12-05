

const sentence1 = 'On July 17, 2014, Malaysia Airlines Flight 17, a Boeing 777-200ER, flying from Amsterdam to Kuala Lumpur, was shot down in an area of Eastern Ukraine near the Ukraine/Russian border during the war in Donbas.'
const sentence2 = 'On July 3, 1988, Iran Air Flight 655, an Iranian Airbus A300-200 airliner, was shot down by two surface-to-air missiles from the U.S. Navy guided missile cruiser USS Vincennes over the Strait of Hormuz.'
const sentence3 = 'On February 19, 2003, an Iranian military Ilyushin Il-76 crashed in mountainous terrain near Kerman in Iran. The official report says bad weather brought the aircraft down.'
const sentence4 = 'On September 1, 1983, a Soviet interceptor Sukhoi Su-15 shot down Korean Air Lines Flight 007, a Boeing 747-230B, bound for Gimpo International Airport in Seoul, South Korea, after it flew into Soviet airspace.'
const sentence5 = 'On July 11, 1991, Nigeria Airways Flight 2120, a Douglas DC-8-61 aircraft operated by Nationair Canada, crashed in Jeddah, Saudi Arabia, after two tires ignited upon takeoff, leading to an in-flight fire.'
const sentence6 = 'On January 1, 1978, a Boeing 747-237B, Air India Flight 855, crashed into the Arabian Sea just off the coast of Bombay, India, killing all 190 passengers and 23 crew on board.'
const sentence7 = 'On April 11, 2018, an Algerian Air Force transport plane crashed shortly after take-off from Boufarik Airport, killing all 247 passengers and 10 crew on board the Ilyushin Il-76.'
const sentence8 = 'On September 26, 1997, an Airbus A300B4-220, Garuda Indonesia Flight 152, which departed from Jakarta, Indonesia, and was preparing to land at Medan, North Sumatra, crashed into mountainous terrain, killing 222 passengers and 12 crew members.'
const sentence9 = 'On August 6, 1997, a Boeing 747-3B5, Korean Air Flight 801, crashed on approach to the international airport in the United States territory of Guam, killing 228 of the 254 people aboard.'
const sentence10 = 'On January 1, 1978, a Boeing 747-237B, Air India Flight 855, crashed into the Arabian Sea just off the coast of Bombay, India, killing all 190 passengers and 23 crew on board.'

const sentence_list = [sentence1, sentence2, sentence3, sentence4, sentence5, sentence6, sentence7, sentence8, sentence9, sentence10]


window.addEventListener('load', function () {
    document.getElementById("loadExample").addEventListener("click", loadExample);
    document.getElementById("IEFromExample").addEventListener("click", IEFromExample);
})

function IEFromExample(){
    let responseTextDataElement = document.getElementById('responseTextData');
    let inputTextAreaValue = document.getElementById('inputTextArea').value;
    responseTextDataElement.innerText = "";

    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/x-www-form-urlencoded");

    let requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };

    const URL = "http://127.0.0.1:5000/"+"run?inputstr=" + inputTextAreaValue
    fetch(URL, requestOptions)
        .then(response => response.text())
        .then(result => {
                console.log("Server response: " + result);
                responseFormater(responseTextDataElement, result);
        })
        .catch(error => console.log('error', error));
}

function loadExample(){
    let element = document.getElementById('inputTextArea');
    element.value = '';

    let num = getRandomInt(10);
    element.value = sentence_list[num];
}

function responseFormater(tag, result){
    //tag.innerHTML = result;
    let parsedResults = JSON.parse(result)
    parsedResults.map( (x) =>{
        for([key, val] of Object.entries(x)) {
            tag.innerHTML +=  '<p class="p-inline '+val+'">'+key+'</p>';
        }
    })

}


function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}
