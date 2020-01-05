$('#post__form__btn').on('click', function(event) {
    postForm = $('#post__form');
    const postTitleInput = $('#post__title__inp');
    const postContentInput = $('#post__content__inp');
    const postTagsInput = $('#post__tags__inp');
    const postTitle = $('#post__title');
    const postContent = $('#post__content');
    const postTags = $('#post__tags');
    postTitleInput.val(postTitle.text());
    postContentInput.val(postContent.text());
    postTagsInput.val(postTags.text());
    postForm.submit();
})