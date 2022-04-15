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
  } else {
    console.log("error");
  }
};
