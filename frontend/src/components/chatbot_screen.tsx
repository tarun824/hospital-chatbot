// import Widget from "rasa-webchat";
"use client";
import { useEffect, useState } from "react";
import Widget from "rasa-webchat";
import { io } from "socket.io-client";
// import { socket } from "../socket";

function ChatbotScreen() {
  // const socket = io("http://localhost:5005");
  // const [isConnected, setIsConnected] = useState(false);
  // const [transport, setTransport] = useState("N/A");

  // useEffect(() => {
  //   socket.on("connect", () => {
  //     console.log("Connected to Socket.IO server");
  //   });
  //   // console.log("initial");
  //   // if (socket.connected) {
  //   //   onConnect();
  //   // }

  //   // function onConnect() {
  //   //   setIsConnected(true);
  //   //   setTransport(socket.io.engine.transport.name);

  //   //   socket.io.engine.on("upgrade", (transport) => {
  //   //     setTransport(transport.name);
  //   //   });
  //   // }

  //   // function onDisconnect() {
  //   //   setIsConnected(false);
  //   //   setTransport("N/A");
  //   // }

  //   // socket.on("connect", onConnect);
  //   // socket.on("disconnect", onDisconnect);

  //   // // return () => {
  //   // // socket.off("connect", onConnect);
  //   // // socket.off("disconnect", onDisconnect);
  //   // // };
  //   // console.log("going thriugh all things ");

  //   socket.on("bot_uttered", (responce) => {
  //     console.log(responce);
  //   });
  // }, []);

  return (
    <Widget
      initPayload={"/greet"}
      socketUrl={"http://localhost:5005"}
      socketPath={"/socket.io/"}
      customData={{ language: "en", user_id: 789, sender_id: "user_789" }}
      title={"Rasa Chatbot"}
      inputTextFieldHint={"Type a message..."}
      hideWhenNotConnected={false}
      onSocketEvent={{
        bot_uttered: (data) => console.log("The bot said:", data), // Log the bot's response
        connect: () => console.log("connection established"),
        disconnect: () => console.log("connection disconnected"),
      }}
      embedded={true}
    />
    // <div>
    //   <button className="bg-sky-500 hover:bg-sky-700 " onClick={() => {}}>
    //     Start Chat
    //   </button>
    //   <div>
    //     <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
    //       First name
    //     </label>
    //     <input
    //       type="text"
    //       id="first_name"
    //       className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    //       placeholder="message"
    //       onChange={() => {
    //         socket.emit("user_uttered", {
    //           message: "hi",
    //         });
    //       }}
    //       required
    //     />
    //   </div>
    // </div>
  );
}
export default ChatbotScreen;
