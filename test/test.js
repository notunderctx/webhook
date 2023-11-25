const url = "https://ca63-102-135-169-127.ngrok-free.app/hook";

const data = {
  message: "..................",
  sender: "choppermanl@gmail.com",
};

fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
})
  .then((response) => response.text())
  .then((data) => {
    console.log("Success:", data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
