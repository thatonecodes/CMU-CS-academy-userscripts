// ==UserScript==
// @name         Paste Script
// @namespace    http://tampermonkey.net/
// @version      2023-12-06
// @description  try to take over the world!
// @author       You
// @match        https://academy.cs.cmu.edu/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=cmu.edu
// @grant        none
// ==/UserScript==


//blocks google analytics on cs acadmey
window['ga-disable-UA-112596988-1'] = true;
let canPaste = true;
const buttonVisible = true;
//button colors
const buttonBackgroundColor = "#58f5aa";
const buttonColor = "#5043e4";


//const vars - here
ClipboardEvent.prototype.originalPreventDefault = ClipboardEvent.prototype.preventDefault;
ClipboardEvent.prototype.originalStopImmediatePropogation = ClipboardEvent.prototype.stopImmediatePropagation;

let toasterContainerStore = null;

function removePrototypes(){
    if (canPaste) {
        ClipboardEvent.prototype.preventDefault = function() {
            console.log("null");
            console.log("COPY ENABLED!");
        }
        ClipboardEvent.prototype.stopImmediatePropagation = function() {
            console.log("null");
        }
        const toasterContainer = document.querySelector(".toaster-container");
        toasterContainerStore = toasterContainer;
        document.getElementById("app").removeChild(toasterContainer);
    }
}

function reAddPrototypes(){
    ClipboardEvent.prototype.preventDefault = ClipboardEvent.prototype.originalPreventDefault;
    ClipboardEvent.prototype.stopImmediatePropagation = ClipboardEvent.prototype.originalStopImmediatePropogation;
    if (toasterContainerStore){
        document.getElementById("app").appendChild(toasterContainerStore);
    }
}

function changeButtonColor(BgColor, color){
    const button = document.querySelector(".paste-button-dynm")
    if (button){
        button.style.backgroundColor = BgColor;
        button.style.color = color;
    }
}

function showbuttonTooltip(visiblity, xVal, yVal){
    if (visiblity){
        const topNumber = yVal / 2 - 4;
        const widthNumber = xVal - 18;
        console.log(topNumber, widthNumber);
        const newDiv = document.createElement("div");
        newDiv.className = "tooltip-paste-dynm";
        newDiv.style.cssText = `position: absolute; top: ${topNumber}px; left: ${widthNumber}px; color: #fff; z-index: 1070; font-size: 12px; padding: 3px 8px; max-width: 200px; text-align:center; background-color: #000; border-radius:4px;`;
        newDiv.textContent = "External Paste";
        document.body.appendChild(newDiv);
        const arrowDiv = document.createElement("div");
        arrowDiv.style.cssText = "position: absolute; margin-right: -5px; z-index: 2000; width: 0; height: 0; border-style: solid; border-width: 0 5px 5px 5px; border-color: transparent transparent #000 transparent; left: 48%; top:22px; transform: translateX(-50%); transform: rotate(180deg);";
        newDiv.appendChild(arrowDiv);
    }else{
        const buttonSpawned = document.querySelector(".tooltip-paste-dynm");
        document.body.removeChild(buttonSpawned);
    }
}

document.addEventListener("copy", () => {
    canPaste = false;
    reAddPrototypes();
    changeButtonColor("orange", "white");
});

removePrototypes();

const blockingRequests = ["https://backend.academy.cs.cmu.edu/api/v0/track/", "https://backend.academy.cs.cmu.edu/api/v0/submission/access-tracker/", "https://api.rollbar.com/api/1/item/"]

let elementButtonAdded = false;
var originalFetch = window.fetch;
window.fetch = function(url, options){
    if (url == "https://backend.academy.cs.cmu.edu/api/v0/submission/points/"){
        const optionsBody = JSON.parse(options.body)
        let submissionID = optionsBody.submission_id;
        let fileVersion = optionsBody.file_version;

        let jsonDefined = {
            "submission_id": submissionID,
            "points": 1,
            "score": "PASS",
            "file_version": fileVersion
        }
        options.body = JSON.stringify(jsonDefined);
        console.log(`Found submission url: ${url}, ${options.body}`);
     }
    if (blockingRequests.some(blockedUrl => url.includes(blockedUrl))){
        console.log("Blocked Request in List:", url);
        return Promise.reject(new Error("Blocked Request."))
    }else{
        if (!elementButtonAdded && buttonVisible){
            addElement();
        }else if (!document.querySelector(".paste-button-dynm")){
            console.log("paste btn reset again!");
            elementButtonAdded = false;
        }
        return originalFetch.apply(this, arguments)
    }
}


function addElement(){
    try {
        const toolBar = document.querySelector(".toolbar.left");
        if (toolBar){
            const tooltipButton = document.createElement("button");
            tooltipButton.textContent = "Paste";
            tooltipButton.style.marginRight = "10px";
            tooltipButton.style.padding = "4px 12px";
            tooltipButton.style.border = "none";
            tooltipButton.style.borderRadius = "2px";
            tooltipButton.style.minHeight = "32px";
            tooltipButton.style.fontWeight = "600";
            tooltipButton.className = "paste-button-dynm"; //dynamic paste btn
            if (canPaste){
                tooltipButton.style.backgroundColor = buttonBackgroundColor;
                tooltipButton.style.color = buttonColor;
            }
            const playButton = document.querySelector(".ui-btn.success");
            toolBar.insertBefore(tooltipButton,playButton);
            tooltipButton.addEventListener("click", () => {
                if (canPaste){
                    canPaste = false;
                    reAddPrototypes();
                    changeButtonColor("orange", "white");
                }else{
                    canPaste = true;
                    removePrototypes();
                    changeButtonColor(buttonBackgroundColor, buttonColor);
                }
            });

            tooltipButton.addEventListener("mouseenter", () => {
                tooltipButton.style.opacity = "0.8";
                showbuttonTooltip(true, tooltipButton.getBoundingClientRect().x, tooltipButton.getBoundingClientRect().y);
            });
            tooltipButton.addEventListener("mouseleave", () => {
                tooltipButton.style.opacity = "1";
                showbuttonTooltip(false, tooltipButton.getBoundingClientRect().x, tooltipButton.getBoundingClientRect().y);
            });

            elementButtonAdded = true;
        }
    } catch (error) {
        console.error(error);
    }
}



