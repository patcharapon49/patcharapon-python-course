TRAVERSE(head):
    current ← head
    WHILE current ≠ None DO
        VISIT(current.data)
        current ← current.next
    END WHILE
END