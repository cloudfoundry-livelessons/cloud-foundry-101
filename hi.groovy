@RestController
class YoDawgRestController {

  @GetMapping("/")
  def hi(){
    return "Hello!"
  }
}
