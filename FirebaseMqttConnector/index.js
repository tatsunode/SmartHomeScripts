var firebase = require("firebase");
var fs = require("fs");
var mqtt = require("mqtt");

function main() {

    var firebaseConfigPath = String(process.env.FIREBASE_CONFIG);
    var authEmail = process.env.FIREBASE_AUTH_EMAIL;
    var authPass = process.env.FIREBASE_AUTH_PASS;
    var mqttServerUrl = "mqtt://" + process.env.MQTT_HOST + ":" + process.env.MQTT_PORT;

    console.log(firebaseConfigPath)

    var config = JSON.parse(fs.readFileSync(firebaseConfigPath));
    firebase.initializeApp(config);

    var mqttClient = mqtt.connect(mqttServerUrl);
    mqttClient.on("connect", () => {
        mqttClient.subscribe("#");

        firebase.auth().signInWithEmailAndPassword(authEmail, authPass)
            .then(function() {
                console.log("mqtt, firebase initialization success")
                // startMqttToFirebase(firebase, mqttClient);
                startFirebaseToMqtt(firebase, mqttClient);
            })
            .catch(function(error) {
                console.log(error.message)
            })
    });
}


var previousMqttToFirebaseTopic;
var previousMqttToFirebaseValue;
var previousFirebaseToMqttTopic;
var previousFirebaseToMqttValue;
// ---
// MQTT -> Firebase
// ---
function startMqttToFirebase(firebase, mqttClient) {
    console.log("startMqttToFirebase");

    mqttClient.on("message", function(topic, message) {

        var value = String(message);

        if (previousFirebaseToMqttTopic != topic || previousFirebaseToMqttValue != value) {
            console.log("MQTT->FIREBASE: " + topic + " " + message);
            firebase.database().ref("/mqtt/" + topic).set(value);
        }

        previousMqttToFirebaseTopic = topic;
        previousMqttToFirebaseValue = value;
    });
}


// ----
// Firebase -> MQTT
// ----
var previousData;
function startFirebaseToMqtt(firebase, mqttClient) {
    console.log("startFirebaseToMqtt");

    firebase.database().ref("/mqtt").on("value", function(snapshot) {

        if (previousData)
            checkDataUpdate(snapshot.val(), previousData, "", mqttClient);

        previousData = snapshot.val();

    });
}

function checkDataUpdate(newData, oldData, path, mqttClient) {

    for (var key in newData) {
        var newValue = newData[key];

        if ((typeof oldData) == "undefined" || oldData == null) {
            var oldValue = null;
        } else {
            var oldValue = oldData[key];
        }

        if ((typeof newValue) == "object") {
            checkDataUpdate(newValue, oldValue, path+"/"+key, mqttClient)

        } else if (newValue != oldValue){

            var topic = path.slice(1) + "/" + key;
            var value = String(newValue);

            if (previousMqttToFirebaseTopic != topic || previousMqttToFirebaseValue != value) {
                console.log("FIREBASE->MQTT: " + topic + " " + value)
                mqttClient.publish(topic, value)
            }
            previousFirebaseToMqttTopic = topic;
            previousFirebaseToMqttValue = value;
        }
    }
}

main()
