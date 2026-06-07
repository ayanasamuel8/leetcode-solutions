/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func createBinaryTree(descriptions [][]int) *TreeNode {
    nodes := make(map[int]*TreeNode)
    ithaveparent := make(map[int]bool)
    for _, description := range descriptions{
        parent := description[0]
        child := description[1]
        flag := description[2] == 1
        if _, exists := nodes[parent]; !exists{
            newNode := &TreeNode{Val: parent}
            var newNodechild *TreeNode
            if childNode, childExists := nodes[child]; childExists {
                newNodechild = childNode
            } else {
                newNodechild = &TreeNode{Val: child}
                nodes[child] = newNodechild
            }
            
            if flag {
                newNode.Left = newNodechild
            } else {
                newNode.Right = newNodechild
            }
            nodes[parent] = newNode
        }else{
            newNode := nodes[parent]
            var newNodechild *TreeNode
            if childNode, childExists := nodes[child]; childExists{
                newNodechild = childNode
            }else{
                newNodechild = &TreeNode{Val: child}
                nodes[child] = newNodechild
            }
            if flag{
                newNode.Left = newNodechild
            }else{
                newNode.Right = newNodechild
            }
        }
        ithaveparent[child] = true
    }
    for _, description := range descriptions{
        if !ithaveparent[description[0]]{
            return nodes[description[0]]
        }
    }
    return nil
}