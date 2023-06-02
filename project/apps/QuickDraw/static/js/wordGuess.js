// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};

// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.

let init = (app) => {

    // This is the Vue data.
    app.data = {
        // Complete as you see fit.
        showWinnerScreen: false,
        showLoserScreen: false,
        guessedWord: "",
        urls: [],
    };

    app.enumerate = (a) => {
        // This adds an _idx field to each element of the array.
        let k = 0;
        a.map((e) => { e._idx = k++; });
        return a;
    };

    // This contains all the methods.
    app.methods = {
        // Complete as you see fit.
        checkGuess() {
            const correctWord = "apple";
            if (this.guessedWord.toLowerCase() === correctWord) {
                this.showWinnerScreen = true; 
                // logic when the guess is correct
            } else {
                // logic when the guess is wrong
                this.showLoserScreen = true;
            }
        }

    };

    // This creates the Vue instance.
    app.vue = new Vue({
        el: "#vue-target",
        data: app.data,
        methods: app.methods
    });

    app.init = () => {
        axios.get('/getImages') // replace with your actual route
        .then(function(r) {
            app.vue.urls = r.data.urls;
            console.log(app.vue.urls)
        })
        .catch(error => {
            console.error(error);
        });
    };

    // Call to the initializer.
    app.init();
};

// This takes the (empty) app object, and initializes it,
// putting all the code in it. 
init(app);
