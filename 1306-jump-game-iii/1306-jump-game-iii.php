class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $start
     * @return Boolean
     */

    function canReach($arr, $start) {
        $n = count($arr);
        $array = array();
        $dp = function($i) use (&$dp, $arr, $n, &$array){
            if ($i < 0 || $i >= $n){
                return False;
            }
            if($arr[$i] == 0){
                return True;
            }
            if (isset($array[$i])){
                return False;
            }
            $array[$i] = True;
            $left = $dp($i + $arr[$i]);
            $right = $dp($i - $arr[$i]);
            if ($left || $right){
                return True;
            }
            return False;
        };
        return $dp($start);
        
    }
}