import 'dart:convert';
import 'package:crm_ui/variable.dart';
import 'package:http/http.dart' as http;

Future<void> sendPostRequest(
    String token, String username, String password) async {
  final Map<String, String> headers = {
    "Content-Type": "application/json",
    "Authorization": "Token $token",
  };

  final Map<String, String> body = {
    "username": username,
    "password": password,
  };

  try {
    final response = await http.post(
      Uri.parse(url),
      headers: headers,
      body: jsonEncode(body),
    );

    if (response.statusCode == 200) {
      print("Request successful: ${response.body}");
    } else {
      print("Request failed with status: ${response.statusCode}");
      print("Response: ${response.body}");
    }
  } catch (e) {
    print("Error occurred: $e");
  }
}


Future<List<Map<String, dynamic>>> fetchData(String path) async {
  final response = await http.get(Uri.parse('$url/$path'));

  if (response.statusCode == 200) {
    Map<String, dynamic> jsonData = jsonDecode(response.body);
    if (jsonData['data'] is List) {
      return List<Map<String, dynamic>>.from(jsonData['data']);
    } else {
      throw Exception('Expected "data" to be a list');
    }
  } else {
    throw Exception('Failed to load data: ${response.statusCode}');
  }
}
