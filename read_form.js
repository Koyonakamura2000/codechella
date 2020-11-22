/*
    When submit button is pressed, form data from html will be sent to app.py
 */

(function() {
    "use strict";

    window.addEventListener("load", init);

    function init() {
        let buttons = document.getElementsByClassName("translatebtn");
        var i;
        for (i = 0; i < buttons.length; i++) {
            buttons[i].addEventListener("click", sendData)
        }
    }

    function sendData() {
        this.innerText = "Clicked on button";
        // organize data to be sent
        let spaceIndex = this.parentNode.id.indexOf(" ");
        let tweetId = this.parentNode.id.substring(0, spaceIndex)
        console.log(tweetId)
        let username = this.parentNode.id.substring(spaceIndex + 1)
        console.log(username)
        let formData = [];
        let i = 0;
        for (i = 0; i < this.parentNode.childNodes.length - 2; i++) {
            formData.push(this.parentNode.childNodes[i].childNodes[0].childNodes[1].value)
        }
        // want to give back tweetId and formData
        sendToPython(tweetId, username, formData)
    }

    function sendToPython(tweetId, username, formData) {
        fetch("http://127.0.0.1:5000/posttweet", {
            headers: {
                "Content-type": "application/json"
            },
            method: "POST",
            body: JSON.stringify({"id": tweetId, "username": username, "formData": formData})
        }).then(function (response) {
            return response.text();
        })
        .then(function (text) {
            console.log('POST response: ');

            // Should be 'OK' if everything was successful
            console.log(text);
        });
    }

})();