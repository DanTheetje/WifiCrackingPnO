function deletePost(postId) {
  fetch("/delete-post", {
    method: "POST",
    body: JSON.stringify({ postId: postId }),
  }).then((_res) => {
    window.location.href = "/post";
  });
}

function donation(postId) {
  fetch("/donate", {
    method: "POST",
    body: JSON.stringify({ postId: postId }),
  }).then((_res) => {
    window.location.href = "/forum";
  });
}
