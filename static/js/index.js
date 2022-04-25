const onPostFormSubmit = (form) => {
  const postsContainer = document.querySelector("#posts-container");
  const postTemplate =
    document.querySelector("#post-template") &&
    document.querySelector("#post-template").content;

  const formData = new FormData(form);

  const data = Object.fromEntries(formData);

  if (formData.get("text").length < 1) {
    document.querySelector("#post-error-length").classList.remove("hidden");
    return;
  }

  document.querySelector("#post-error-length").classList.add("hidden");

  console.log(data);
  fetch(form.action, {
    method: "post",
    body: JSON.stringify(data),
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

        postContent.textContent = formData.get("text");

        postClone.querySelector(".post").id = postId;

        const buttonDelete = postClone.querySelector(".button--delete");

        buttonDelete.addEventListener("click", () => deletePost(postId));

        postsContainer.prepend(postClone);

        form.reset();

        highlightHashtags();

        animate(postElement);
      }
    })
    .catch((error) => {
      console.error(error);
    });
};

const animate = (postElement) => {
  const postsContainer = document.querySelector("#posts-container");
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

//highlightHashtags();
