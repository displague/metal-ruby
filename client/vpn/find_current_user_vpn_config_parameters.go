// Code generated by go-swagger; DO NOT EDIT.

package vpn

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"
)

// NewFindCurrentUserVPNConfigParams creates a new FindCurrentUserVPNConfigParams object
// with the default values initialized.
func NewFindCurrentUserVPNConfigParams() *FindCurrentUserVPNConfigParams {
	var ()
	return &FindCurrentUserVPNConfigParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewFindCurrentUserVPNConfigParamsWithTimeout creates a new FindCurrentUserVPNConfigParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewFindCurrentUserVPNConfigParamsWithTimeout(timeout time.Duration) *FindCurrentUserVPNConfigParams {
	var ()
	return &FindCurrentUserVPNConfigParams{

		timeout: timeout,
	}
}

// NewFindCurrentUserVPNConfigParamsWithContext creates a new FindCurrentUserVPNConfigParams object
// with the default values initialized, and the ability to set a context for a request
func NewFindCurrentUserVPNConfigParamsWithContext(ctx context.Context) *FindCurrentUserVPNConfigParams {
	var ()
	return &FindCurrentUserVPNConfigParams{

		Context: ctx,
	}
}

// NewFindCurrentUserVPNConfigParamsWithHTTPClient creates a new FindCurrentUserVPNConfigParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewFindCurrentUserVPNConfigParamsWithHTTPClient(client *http.Client) *FindCurrentUserVPNConfigParams {
	var ()
	return &FindCurrentUserVPNConfigParams{
		HTTPClient: client,
	}
}

/*FindCurrentUserVPNConfigParams contains all the parameters to send to the API endpoint
for the find current user Vpn config operation typically these are written to a http.Request
*/
type FindCurrentUserVPNConfigParams struct {

	/*Code
	  Facility code

	*/
	Code string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the find current user Vpn config params
func (o *FindCurrentUserVPNConfigParams) WithTimeout(timeout time.Duration) *FindCurrentUserVPNConfigParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the find current user Vpn config params
func (o *FindCurrentUserVPNConfigParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the find current user Vpn config params
func (o *FindCurrentUserVPNConfigParams) WithContext(ctx context.Context) *FindCurrentUserVPNConfigParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the find current user Vpn config params
func (o *FindCurrentUserVPNConfigParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the find current user Vpn config params
func (o *FindCurrentUserVPNConfigParams) WithHTTPClient(client *http.Client) *FindCurrentUserVPNConfigParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the find current user Vpn config params
func (o *FindCurrentUserVPNConfigParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithCode adds the code to the find current user Vpn config params
func (o *FindCurrentUserVPNConfigParams) WithCode(code string) *FindCurrentUserVPNConfigParams {
	o.SetCode(code)
	return o
}

// SetCode adds the code to the find current user Vpn config params
func (o *FindCurrentUserVPNConfigParams) SetCode(code string) {
	o.Code = code
}

// WriteToRequest writes these params to a swagger request
func (o *FindCurrentUserVPNConfigParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// query param code
	qrCode := o.Code
	qCode := qrCode
	if qCode != "" {
		if err := r.SetQueryParam("code", qCode); err != nil {
			return err
		}
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
