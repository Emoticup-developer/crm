import 'package:crm_ui/homepage/homepage.dart';
import 'package:crm_ui/login/login.dart';
import 'package:crm_ui/variable.dart';
import 'package:flutter/material.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:path_provider/path_provider.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final appDocDir = await getApplicationDocumentsDirectory();
  await Hive.initFlutter(appDocDir.path);
  await load_data();
  runApp(MyApp());
}

load_data() async {
  var box = await Hive.openBox('myBox');

  is_login = box.get("login");
  await Future.delayed(Duration(seconds: 2));
}

// ignore: must_be_immutable
class MyApp extends StatelessWidget {
  MyApp({super.key});

  // ignore: non_constant_identifier_names

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
            seedColor: const Color.fromARGB(255, 209, 209, 209)),
        useMaterial3: true,
      ),
      // home: LoginPage(),
      home: is_login ? HomePage() : LoginPage(),
    );
  }
}
