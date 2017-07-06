@RestController
class GreetingsRestController {

  @GetMapping("/hi/{name}")
  def hi(@PathVariable String name){
    [ greeting : "Hello, " + name +"!" ]
  }
}
