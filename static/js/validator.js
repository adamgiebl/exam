function _all(q, e = document) {
  return e.querySelectorAll(q);
}
function _one(q, e = document) {
  return e.querySelector(q);
}

const submitLoginForm = (form) => {
  form.submit();
};
// ##############################
function validate(form, callback = null) {
  let error = false;
  _all("[data-validate]", form).forEach(function (element) {
    element.classList.remove("validate_error");
  });
  _all("[data-validate]", form).forEach(function (element) {
    switch (element.getAttribute("data-validate")) {
      case "str":
        if (
          element.value.length < parseInt(element.getAttribute("data-min")) ||
          element.value.length > parseInt(element.getAttribute("data-max"))
        ) {
          element.classList.add("validate_error");
          error = true;
        }
        break;
      case "int":
        if (
          !/^\d+$/.test(element.value) ||
          parseInt(element.value) <
            parseInt(element.getAttribute("data-min")) ||
          parseInt(element.value) > parseInt(element.getAttribute("data-max"))
        ) {
          element.classList.add("validate_error");
          error = true;
        }
        break;
      case "email":
        let re =
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (!re.test(element.value.toLowerCase())) {
          element.classList.add("validate_error");
          error = true;
        }
        break;
      case "re":
        var regex = new RegExp(element.getAttribute("data-re"));
        if (!regex.test(element.value)) {
          console.log("phone error");
          element.classList.add("validate_error");
          error = true;
        }
        break;
      case "match":
        if (
          element.value !=
          _one(`[name='${element.getAttribute("data-match-name")}']`, form)
            .value
        ) {
          element.classList.add("validate_error");
          error = true;
        }
        break;
    }
  });
  if (error) {
    return false;
  }
  if (!_one(".validate_error", form)) {
    callback && callback(form);
    return true;
  }
  // _one(".validate_error", form).focus()
}

// ##############################
function clear_validate_error() {
  // event.target.classList.remove("validate_error")
  // event.target.value = ""
}
