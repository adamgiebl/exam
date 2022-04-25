const showTweetModal = () => {
  document.querySelector(".modal-overlay").style.display = "block";
};

const closeTweetModal = () => {
  document.querySelector(".modal-overlay").style.display = "none";
};

const deletePost = async (id) => {
  const response = await fetch(`/posts/delete/${id}`, { method: "DELETE" });

  if (response.ok) {
    document.querySelector(`[id='${id}']`).remove();
  }
};

const follow = async (el) => {
  el.classList.add("loading");
  console.log("following");

  const username = el.dataset.username;

  const response = await fetch(`/follow/${username}`, { method: "POST" });

  if (response.ok) {
    console.log("done");

    el.classList.remove("loading");

    el.classList.add("done");
  } else {
    console.log("error");
  }
};

const togglePostEdit = (button) => {
  console.log("clicked");
  const post = button.closest("article.post");
  button.classList.toggle("active");
  post.classList.toggle("edit-mode");
};

const confirmEditPost = async (button) => {
  const post = button.closest("article.post");
  const text = post.querySelector(".post__content--edit").value;
  const postId = post.id;
  const postContent = post.querySelector("div.post__content");
  const buttonEdit = post.querySelector(".button--edit");

  const response = await fetch("/edit-post", {
    method: "post",
    body: JSON.stringify({ text, postId }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    postContent.textContent = text;
    post.classList.remove("edit-mode");
    buttonEdit.classList.remove("active");
  }
};
