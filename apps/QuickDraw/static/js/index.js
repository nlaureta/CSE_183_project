// This will be the object that will contain the Vue attributes
// and be used to initialize it.
let app = {};

// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.

let init = (app) => {

    // This is the Vue data.
    app.data = {
        // Complete as you see fit.
        word: '',// get random word that does not drawn by user
    };

    app.enumerate = (a) => {
        // This adds an _idx field to each element of the array.
        let k = 0;
        a.map((e) => { e._idx = k++; });
        return a;
    };

    // This contains all the methods.
    app.methods = {
        saveAndConfirm: (word) => {
            window.saveCanvas(word);
            confirm('You have saved the canvas');
        },
    };

    // This creates the Vue instance.
    app.vue = new Vue({
        el: "#vue-target",
        data: app.data,
        methods: app.methods
    });

    app.init = () => {
        axios.get('/getWords')
        .then(function(r) {
            app.vue.word = r.data.word;
            console.log(app.vue.word)
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
