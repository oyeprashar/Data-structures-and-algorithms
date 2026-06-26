class Solution:

    """
    maxPagesLimit : is the max no of pages a students is allowed to read
    We find the no of students needed such that this max limit is obeyed 

    If the number of students needed to obey this limit is greator than input, we return false
    """

    def isValid(self, maxPagesLimit, pages, noOfStudents):
        """

        :param maxPages: maxPage a student reads
        :param pages: array of the books
        :param noOfStudents: total students we need to allocate books to
        :return: True/False
        """

        studentsNeeded = 1
        currPagesRead = 0

        for page in pages:

            # a book is greator than the limit and this limit cannot be valid
            if page > maxPagesLimit:
                return False

            # Make the current student read this book
            currPagesRead += page

            # if the student read more than the limit, increment students needed and make that student read this book
            if currPagesRead > maxPagesLimit:
                studentsNeeded += 1
                currPagesRead = page # since last student was not able to read this, next student starts from here

            # we needed more students than allowed
            if studentsNeeded > noOfStudents:
                return False
    
        return True
        

    """
    Binary search over the answer space and trying to minimise it
    """
    def binarySearchOnAnswer(self, left, right, pages, noOfStudents, ans):

        if left <= right:

            mid = (left + right) // 2

            if self.isValid(mid, pages, noOfStudents):
                # save and move left to minimise this
                ans[0] = min(ans[0], mid)
                return self.binarySearchOnAnswer(left, mid - 1, pages, noOfStudents, ans)

            else:
                return self.binarySearchOnAnswer(mid + 1, right, pages, noOfStudents, ans)


    def findPages(self, pages, noOfStudents):
        
        if noOfStudents > len(pages):
            return -1

        left = max(pages) # when k == n, then each students reads one book from the array.
        right = sum(pages) # when k = 1, one student reads all the books
        ans = [3**38]
        self.binarySearchOnAnswer(left, right, pages, noOfStudents, ans)
        return ans[0]

