import { Routes } from '@angular/router';
import { RegistrationComponent } from './register/registration/registration.component';
import { LoginComponent } from './auth/login/login.component';
import { HomeComponent } from './contents/home/home.component';
import { LayoutComponent } from './shared/layout/layout.component';
import { LogoutComponent } from './auth/logout/logout.component';
import { ManageComponent } from './contents/manage/manage.component';
import { SettingsComponent } from './contents/settings/settings.component';
import { StatusComponent } from './contents/status/status.component';

export const routes: Routes = [
    { path: 'app',
        component: LayoutComponent,
        children: [
            { path: '', component: HomeComponent },
            { path: 'register', component: RegistrationComponent, },
            { path: 'login', component: LoginComponent, },
            { path: 'logout', component: LogoutComponent, },
            { path: 'manage', component: ManageComponent, },
            { path: 'settings', component: SettingsComponent, },
            { path: 'status', component: StatusComponent, },
        ],
    },
    { path: '**', redirectTo: 'app' },
];
