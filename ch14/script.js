function greet(name) {
  const message = "こんにちは、" + name + "さん！";
  document.getElementById("message").textContent = message;
}

document.getElementById("hello").addEventListener("click", function () {
  greet("ゲスト");
});
