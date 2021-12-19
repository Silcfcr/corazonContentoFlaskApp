console.log(window);

function play(element) {
    document.this.play();
}

function pause(element) {
    document.this.pause();
}

document.getElementsById("myVid1").addEventListener("mouseover", function() {
	this.play();
});

document.getElementsById("myVid1").addEventListener("mouseleave", function() {
	this.pause();
});