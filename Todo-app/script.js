// HTMLの道具を「地図(DOM)から探す」
const input = document.querySelector("#todo-input");     // 入力欄
const addButton = document.querySelector("#add-button"); // 追加ボタン
const list = document.querySelector("#todo-list");       // リストの入れ物

function addTodo() {
  const text = input.value.trim();
  if (text === "") return;

  // li（1行の入れ物）
  const li = document.createElement("li");

  // チェックボックス
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";

  // チェックされたら見た目を変える
  checkbox.addEventListener("change", function () {
    li.classList.toggle("completed"); 
  });

  // テキスト部分
  const span = document.createElement("span");
  span.textContent = text;

  // 削除ボタン
  const deleteBtn = document.createElement("button");
  deleteBtn.textContent = "削除";
  deleteBtn.addEventListener("click", function () {
    li.remove();
  });

  // li に順番に入れる（チェック → テキスト → 削除）
  li.appendChild(checkbox);
  li.appendChild(span);
  li.appendChild(deleteBtn);

  // リストに追加
  list.appendChild(li);

  input.value = "";
}



// 「追加ボタンが押されたら、addTodoという箱を開ける」
addButton.addEventListener("click", addTodo);
// Enterキーが押されたら addTodo を実行する
input.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    addTodo();
  }
});
