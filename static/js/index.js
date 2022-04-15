const form = document.querySelector("#post-form");
//const fakePostsContainer = document.querySelector("#fake-posts-container");
const postsContainer = document.querySelector("#posts-container");
const postTemplate =
  document.querySelector("#post-template") &&
  document.querySelector("#post-template").content;

if (postsContainer && form) {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    fetch(form.action, {
      method: "post",
      body: JSON.stringify(Object.fromEntries(formData)),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then(async (result) => {
        if (result.ok) {
          const postId = await result.text();
          const postClone = postTemplate.cloneNode(true);
          const postElement = postClone.firstElementChild;

          const postContent = postClone.querySelector(".post__content");
          const postTextarea = postClone.querySelector(
            ".post__textarea .textarea"
          );

          postContent.textContent = formData.get("text");

          postTextarea.textContent = formData.get("text");

          postClone.querySelector(".post").id = postId;

          const buttonLabel = postClone.querySelector(".button--edit__label");
          const buttonEdit = postClone.querySelector(".button--edit");
          const buttonDelete = postClone.querySelector(".button--delete");

          buttonEdit.addEventListener("click", (e) => {
            buttonLabel.textContent = "Save";
            buttonEdit.classList.add("active");
            postContent.style.display = "none";
            postTextarea.parentElement.style.display = "block";
          });

          buttonDelete.addEventListener("click", async (e) => {
            const response = await fetch(`/posts/delete/${postId}`, {
              method: "DELETE",
            });

            if (response.ok) {
              document.querySelector(`[id='${postId}']`).remove();
            }
          });

          postsContainer.prepend(postClone);

          form.reset();

          highlightHashtags();

          animate(postElement);
        }
      })
      .catch((error) => {
        console.error(error);
      });
  });
} else {
  console.log("No posts container");
  form &&
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const formData = new FormData(form);
      fetch(form.action, {
        method: "post",
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
          "Content-Type": "application/json",
        },
      }).then(() => {
        document.location.reload();
      });
    });
}

const animate = (postElement) => {
  const startPos = document
    .querySelector("#submit-button")
    .getBoundingClientRect();

  const endPos = postElement.getBoundingClientRect();

  const difX =
    startPos.left - endPos.left + startPos.width / 2 - endPos.width / 2;
  const difY =
    startPos.top - endPos.top + startPos.height / 2 - endPos.height / 2;

  postsContainer.style.transition = `none`;

  postElement.style.transform = `translate(${difX}px, ${
    difY + 100
  }px) scale(0.1, 0.5)`;
  postElement.style.opacity = `1`;

  if (document.querySelector(".post--empty")) {
    document.querySelector(".post--empty").classList.add("hidden");
  }

  postsContainer.style.transform = `translateY(-${endPos.height}px)`;

  requestAnimationFrame(() => {
    postElement.style.transition = `all 0.5s cubic-bezier(0.660, 0.140, 0.255, 1.2)`;
    postElement.style.transform = `translate(0, 0)`;
    postElement.style.opacity = `1`;
    postsContainer.style.transition = `all 0.4s linear`;
    postsContainer.style.transform = `translate(0, 0)`;
  });
};

const highlightHashtags = () => {
  document.querySelectorAll(".post__content").forEach((el) => {
    el.innerHTML = el.textContent.replace(
      /(^|\W)(#.*?(?= #|$))/gi,
      "$1<span>$2</span>"
    );
  });
};

highlightHashtags();
