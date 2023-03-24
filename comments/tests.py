from testing.testcases import TestCase


class CommonModelTests(TestCase):

    def setUp(self):
        self.clear_cache()
        self.sherry = self.create_user('sherry')
        self.tweet = self.create_tweet(self.sherry)
        self.comment = self.create_comment(self.sherry, self.tweet)

    def test_comment(self):
     
        # """Fail if the two objects are equal as determined by the '!='
        #    operator.
        self.assertNotEqual(self.comment.__str__, None)

    def test_like_set(self):
        self.create_like(self.sherry, self.comment)
        self.assertEqual(self.comment.like_set.count(), 1)

        self.create_like(self.sherry, self.comment)
        self.assertEqual(self.comment.like_set.count(), 1)

        mary = self.create_user('mary')
        self.create_like(mary, self.comment)
        self.assertEqual(self.comment.like_set.count(), 2)