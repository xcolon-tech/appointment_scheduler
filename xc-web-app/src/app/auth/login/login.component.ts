import { Component } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  data: any;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    // GET request
    this.apiService.getApi('items').subscribe(response => {
      this.data = response;
    });

    // POST request
    const newItem = { name: 'New Item', description: 'This is a new item' };
    this.apiService.postApi('items', newItem).subscribe(response => {
      console.log('Item created:', response);
    });

    // PUT request
    const updatedItem = { name: 'Updated Item', description: 'This item has been updated' };
    this.apiService.updateApi('items/1', updatedItem).subscribe(response => {
      console.log('Item updated:', response);
    });

    // DELETE request
    this.apiService.deleteApi('items/1').subscribe(response => {
      console.log('Item deleted:', response);
    });
  }

}
